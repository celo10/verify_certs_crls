'''
Criado por: Marcelo Batista
Mantido por: Marcelo Batista
Em: 02-10-2024
'''

log_config = {
    # Parte da documentacao desta configuracao pode ser consultada na documentacao da biblioteca do logging do python
    "log_enable" : "False",                # Se "True" - Habilita Log / Se "False" - Desabilita log
    "level"      : "logging.INFO",        # Qual o nivel de Logging (Padrão e INFO, outros na doc oficial da lib logging do python)
    "log_path"   : "./",                  # Qual o dir em que o arquivo de log sera armazenado, uma opcao é "/var/log" mas precisa de permissao
    "log_file"   : "crl_verifier_{}.log", # Nome do arquivo de log, o padrao e rotacionar por ano mes dia
    "encoding"   : "utf-8",               # Qual mapeamento de caracteres os logs serao escritos
    "filemode"   : "a",                   # Tipo de modo de criacao do arquivo de log: "a" create+apend
    "format"     : "%(asctime)s %(levelname)s %(message)s", # Formato da linha de log
    "datefmt"    : "%Y%m%d-%H:%M:%S"      # Formato da data na linha de log
}