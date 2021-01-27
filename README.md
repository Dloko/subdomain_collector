# subdomain_collector
O subdomain_collector serve para você descobrir subdomínios de um domínio	específico.


# Como Usar.
Ao executar o código ira aparecer um “@”, na frente dele você escrevera o domino (sem www, gov e etc.), ele ira procura subdomínios do domínio que você digitou
se não tiver arquivo criado ele ira criar 2 arquivos um chamado "subdomain" para amazenar as informações e cria um "subdomain2" que pega oque ta no "subdomain"
e filtra para que não fique informações desnecesraia

# Como funciona(básico)
O código usa bibliotecas em Python como “subprocess” e “multiprocess” e também algumas ferramentas do linux listada no “requirements” Filtra as informações usado “|grep”, ”cut” e “sort”.
