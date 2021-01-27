# subdomain_collector
O subdomain_collector serve para você descobrir subdomínios de um domínio	específico.


# Como Usar.
Ao executar o código íra aparecer um “@”, na frente dele você escrevera o domínio (sem www, gov e etc.), ele irá procurar subdomínios do domínio que você digitou
se não tiver um arquivo criado, ele irá criar 2 arquivos, um chamado "subdomain" para amazenar as informações é criar um "subdomain2" que pega o que tiver no "subdomain" e filtra para que não fique informações desnecessárias.

# Como funciona(básico)
O código usa bibliotecas em Python como “subprocess” e “multiprocess” e também algumas ferramentas do linux listadas no “requirements”. e Filtra as informações usando “|grep”, ”cut” e “sort”.
