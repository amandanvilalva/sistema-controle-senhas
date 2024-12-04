# Sistema de Controle de Senhas

## Objetivo
Um programa que organiza senhas de usuários para diferentes serviços de forma segura.

## Funcionalidades
1. Armazenar senhas com criptografia simples.
2. Recuperar senhas com autenticação.
3. Gerar senhas seguras automaticamente.
4. Exportar os dados criptografados para backup.

## Cronograma de Desenvolvimento
| Etapa                  | Prazo  |
|------------------------|--------|
| Configuração inicial   | 1 dia  |
| Armazenar senhas       | 2 dias |
| Gerar senhas seguras   | 1 dia  |
| Recuperar senhas       | 2 dias |
| Exportar backup        | 1 dia  |

---

## **Desafios Enfrentados**
1. **Gerenciamento de branches**: Durante o desenvolvimento, precisei aprender a criar branches independentes para cada funcionalidade e garantir que elas fossem mergeadas corretamente.
2. **Mensagens de commits**: Focar em escrever mensagens claras e informativas para os commits foi algo que precisei aperfeiçoar. No início, fiz commits mais genéricos, mas ajustei para que cada mensagem descrevesse exatamente o que foi implementado.
3. **Implementação da criptografia**: Escolher uma forma simples e eficiente de criptografar senhas foi desafiador. Optei pelo uso do módulo `base64` para simplificar o processo inicial, com intenção de melhorias futuras.
4. **Exportação de dados**: Implementar uma funcionalidade que exportasse os dados com segurança sem comprometer a integridade dos arquivos exigiu atenção extra.

---

## **Como o Git me ajudou**
1. **Organização**: O Git foi essencial para dividir o projeto em etapas claras. Criar uma branch para cada funcionalidade me permitiu trabalhar de forma independente em diferentes partes do sistema sem interferir no código principal.
2. **Histórico de mudanças**: Pude acompanhar facilmente todas as alterações feitas no projeto, o que ajudou a identificar e corrigir problemas rapidamente.
3. **Resolução de conflitos**: Durante os merges, enfrentei pequenos conflitos de código. Graças ao Git, consegui resolvê-los de forma eficiente, garantindo que o projeto permanecesse funcional.
4. **Documentação**: Utilizar commits frequentes e bem documentados facilitou a criação de um histórico detalhado do projeto, o que será útil para melhorias futuras.
5. **Backup seguro**: Com o repositório no GitHub, tive a tranquilidade de saber que todo o progresso estava salvo remotamente, reduzindo os riscos de perda de dados.