# Script de consolidação dos dados - Teste Mobi7

## Instalar as dependencias

```bash
pip install -r requirements.txt
```
## Rodar o docker para o banco estar ativo e com dados
Seguir as orientações contidas no arquivo  [Code Test description](https://github.com/Andresscorrea/Mobi7_test/blob/main/Docs/Code%20Test%20Description.docx) , para inicializar o banco.

## rodar o script
```bash
python src/main.py
```

## Resultados
O script criará uma tabel chamada consolided_values coms os dados consolidados, e no campo day constará o dia e hora da execução
No final do script será gerado o arquivo resultado.csv

Depois de populado o banco, dentro do arquivo power bi(Mobi7_test.pbix) basta dar um refresh nos dados para ver os resultados da última atualização


