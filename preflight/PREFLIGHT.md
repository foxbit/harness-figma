# Preflight — Reconstrução Incremental de Componentes

Este documento rege o escopo de **preflight**: a reconstrução de um
componente do arquivo Legado para o arquivo de Produção, seguindo
`COMPONENT_STANDARDS.md` desde o início. Ao contrário do onboarding
(que roda uma vez, é só leitura), o preflight roda **sob demanda,
incrementalmente**, e escreve de fato no arquivo de Produção.

Ver `CLAUDE.md` para como este escopo se relaciona com Onboarding e
Produção, e para a mecânica de "MIGRAR DO LEGADO" dentro do fluxo
normal de produção.

---

## Por que incremental, não em lote (big-bang)

Reconstruir todo o design system legado de uma vez, antes de qualquer
entrega, arriscaria gastar esforço em componentes que talvez nunca
sejam usados de novo. O preflight roda **um componente (ou pequeno
grupo) por vez**, disparado por uma necessidade real:

1. Uma jornada de produção nova, cujo `interpreter` classificou um
   elemento como `MIGRAR DO LEGADO`
2. Uma priorização manual a partir do `migration-backlog.md` gerado
   pelo onboarding (ex: você decide adiantar a migração de componentes
   de alta prioridade antes mesmo de a demanda aparecer)

## Quando o preflight cria o arquivo de Produção

Na primeira reconstrução de um componente para um cliente que ainda não
tem arquivo de Produção, o `preflight-builder` cria o arquivo antes de
reconstruir qualquer coisa — nunca acumula reconstruções soltas para só
depois decidir criar o projeto. Ver estrutura de páginas em
`CLAUDE.md`.

## Fluxo (agentes correspondentes)

```
1. preflight-planner   → lê o componente no legado, propõe reconstrução
2. [ aprovação humana — inclui avaliar risco de drift visual apontado ]
3. preflight-builder    → reconstrói no arquivo de Produção
4. documenter (de produção) → atualiza Status: em revisão → ativo
```

## Reconstruir, não duplicar

"Duplicar" copiaria a estrutura problemática do legado (tokens
hardcoded, falta de Auto Layout, nomenclatura ruim). O preflight sempre
**reconstrói** — usa o legado como referência visual, mas constrói do
zero seguindo os padrões do sistema novo. Drift visual sutil entre
original e reconstrução é esperado e deve ser destacado para aprovação
consciente, não tratado como erro.

## Governança da coexistência entre os dois sistemas

O arquivo Legado permanece intacto e nunca é editado. Ele continua
sendo referência para telas ainda não migradas. O `PROJECT.md` de cada
cliente mantém um campo de status de migração registrando o que já é
fonte de verdade no arquivo de Produção e o que ainda depende do
Legado — isso é comunicação para humanos (você e o time do cliente), não
algo que o harness resolve sozinho.

## O que o preflight explicitamente NÃO faz

- Não decide quais componentes migrar por conta própria — sempre
  disparado por demanda real (produção) ou priorização manual sua
- Não edita o arquivo Legado, nunca
- Não avalia se a tela toda "faz sentido" — isso é o `validator`, que
  roda depois, no fluxo de produção normal
