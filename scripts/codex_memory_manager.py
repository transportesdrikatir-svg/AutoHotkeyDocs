#!/usr/bin/env python3
"""Memoria local simples para Codex.

Guarda regras e tarefas em .codex/memory.json para evitar repetir processos.
Uso rapido:
  python scripts/codex_memory_manager.py list
  python scripts/codex_memory_manager.py add-rule "Regra importante"
  python scripts/codex_memory_manager.py add-task "descricao da tarefa" --note "resultado"
  python scripts/codex_memory_manager.py search "palavra"
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MEMORY_PATH = ROOT / ".codex" / "memory.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def default_memory() -> dict[str, Any]:
    return {
        "version": 1,
        "rules": [],
        "tasks": [],
    }


def load_memory() -> dict[str, Any]:
    if not MEMORY_PATH.exists():
        return default_memory()
    try:
        data = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        data = default_memory()
    data.setdefault("version", 1)
    data.setdefault("rules", [])
    data.setdefault("tasks", [])
    return data


def save_memory(data: dict[str, Any]) -> None:
    MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    MEMORY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def add_rule(text: str) -> None:
    data = load_memory()
    normalized = text.strip()
    if not normalized:
        raise SystemExit("Regra vazia.")
    for item in data["rules"]:
        if item.get("text", "").strip().lower() == normalized.lower():
            print("Regra ja existia. Nada alterado.")
            return
    data["rules"].append({"text": normalized, "created_at": now_iso()})
    save_memory(data)
    print("Regra guardada.")


def add_task(description: str, note: str = "") -> None:
    data = load_memory()
    desc = description.strip()
    if not desc:
        raise SystemExit("Descricao vazia.")
    data["tasks"].append({"description": desc, "note": note.strip(), "created_at": now_iso()})
    save_memory(data)
    print("Tarefa guardada.")


def search(query: str) -> None:
    data = load_memory()
    q = query.strip().lower()
    if not q:
        raise SystemExit("Pesquisa vazia.")
    found = False
    for section in ("rules", "tasks"):
        for item in data.get(section, []):
            text = json.dumps(item, ensure_ascii=False).lower()
            if q in text:
                found = True
                print(f"[{section}] {json.dumps(item, ensure_ascii=False)}")
    if not found:
        print("Nada encontrado.")


def list_memory() -> None:
    data = load_memory()
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Gerir memoria local de Codex.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="Mostrar memoria completa")

    p_rule = sub.add_parser("add-rule", help="Adicionar regra")
    p_rule.add_argument("text")

    p_task = sub.add_parser("add-task", help="Adicionar tarefa feita")
    p_task.add_argument("description")
    p_task.add_argument("--note", default="")

    p_search = sub.add_parser("search", help="Procurar na memoria")
    p_search.add_argument("query")

    args = parser.parse_args()
    if args.command == "list":
        list_memory()
    elif args.command == "add-rule":
        add_rule(args.text)
    elif args.command == "add-task":
        add_task(args.description, args.note)
    elif args.command == "search":
        search(args.query)


if __name__ == "__main__":
    main()
