# AGENTS.md

## Modo permanente de poupanca de creditos para Codex

Estas regras devem ser lidas antes de qualquer tarefa neste repositorio. O objetivo e reduzir trabalho repetido e evitar gasto desnecessario, sem prometer que o trabalho sera gratis ou sem creditos.

## Regra principal

Codex deve fazer apenas o que foi pedido pelo utilizador. Nao deve acrescentar analises, renomeacoes, conversoes, relatorios longos, organizacoes, pesquisas amplas ou passos extra sem pedido claro.

## Antes de comecar qualquer tarefa

1. Ler este `AGENTS.md`.
2. Ler `.codex/config.toml`, se existir.
3. Verificar scripts existentes em `scripts/` antes de criar novos.
4. Consultar `.codex/memory.json`, se existir, usando `scripts/codex_memory_manager.py` quando possivel.
5. Reutilizar instrucoes, scripts e processos ja existentes antes de procurar ou criar algo novo.
6. Fazer um plano curto so com objetivo, ficheiros necessarios, verificacao minima e resultado esperado.

## Regras de trabalho

- Usar portugues ou espanhol simples.
- Trabalhar sempre com mudancas pequenas e dirigidas.
- Evitar exploracao geral do repositorio quando uma leitura dirigida bastar.
- Nao repetir buscas nem tarefas ja feitas.
- Nao usar subagentes salvo pedido claro do utilizador.
- Nao fazer builds, testes grandes ou verificacoes caras sem necessidade.
- No final, responder so com o essencial: o que foi criado/alterado, como usar e se ficou algo pendente.
- Se uma regra nova for aprendida durante o trabalho, guardar em `AGENTS.md` ou em `.codex/memory.json` para nao repetir o erro.

## Aplicacoes que Codex pode precisar

Codex deve usar apenas as aplicacoes necessarias para cumprir o pedido exato. Nao deve abrir nem consultar aplicacoes extras por iniciativa propria.

Aplicacoes principais permitidas quando forem necessarias:

- GitHub/Codex: para ler e alterar ficheiros do repositorio.
- WhatsApp no computador: fonte principal para ficheiros recebidos quando o pedido for baixar/descarregar.
- Desktop/Escritorio: destino principal para guardar ficheiros baixados, dentro da pasta indicada pelo utilizador.
- Python: apenas para scripts simples do projeto, memoria local e verificacoes pequenas.
- Google Drive: usar apenas se o utilizador pedir claramente Google Drive ou disser que o ficheiro esta no Google Drive.

Aplicacoes que nao deve usar sem pedido claro:

- Google Drive, se o pedido nao mencionar Google Drive.
- Navegador ou internet para pesquisar, se o pedido puder ser feito com ficheiros/instrucoes locais.
- Ferramentas de conversao, OCR, renomeacao, analise ou organizacao, se o utilizador pediu apenas baixar.
- Subagentes ou automatizacoes complicadas, salvo pedido explicito.

## Regra especial para baixar/descarregar ficheiros

Quando o utilizador pedir apenas para baixar/descarregar ficheiros:

1. Procurar primeiro no WhatsApp que esta no computador.
2. Usar Google Drive apenas se o utilizador pedir claramente "Google Drive" ou disser que o ficheiro esta no Google Drive.
3. Baixar apenas para uma pasta no Desktop com o nome indicado pelo utilizador.
4. Nao analisar, renomear, converter, organizar, resumir nem fazer passos extra.
5. Se houver URL direto, usar `scripts/codex_download_only.py` quando fizer sentido.
6. Se o pedido nao trouxer nome de pasta, usar o nome indicado no pedido; se nao houver nenhum nome claro, pedir so esse detalhe.

## Memoria local do projeto

A memoria persistente deste repositorio deve ficar em `.codex/memory.json`. Codex deve consultar essa memoria antes de repetir buscas ou processos. Esta memoria e local do repositorio; nao assumir memoria externa ou de nuvem se ela nao estiver disponivel.

## Frase curta para ativar este modo

Ativa modo poupanca de creditos. Le primeiro `AGENTS.md`, `.codex/config.toml`, scripts e memoria local. Nao repitas buscas nem tarefas. Faz so o que foi pedido. Usa apenas as aplicacoes necessarias. Nao uses subagentes nem relatorios longos. Se for apenas baixar, procura primeiro no WhatsApp do computador e baixa apenas para a pasta indicada no Desktop. Usa Google Drive so se for pedido claramente. Nao facas analise, renomeacao ou passos extra.
