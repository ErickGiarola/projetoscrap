Web Scraping e ELT

Gostaria de compartilhar meu mais recente projeto, no qual desenvolvi um código em Python para realizar web scraping no Mercado Livre. O objetivo principal foi criar uma base de dados bruta, permitindo a coleta das informações dos produtos disponíveis no site.

Após a extração dos dados, armazenei essas informações em um Data Lake fictício, explorando técnicas de manipulação de dados. Em seguida, utilizei SQL para tratar e transformar esses dados, organizando-os para facilitar a futura análise em um Data Warehouse.

💡 Objetivos do Projeto:

Coleta de Dados: Iniciei o projeto com a extração de informações relevantes sobre os produtos do Mercado Livre. Utilizando técnicas de web scraping, desenvolvi um script em Python que coleta dados dos produtos. Esse processo não apenas me ajudou a entender como funciona o scraping, mas também a importância de uma coleta de dados bem realizada.

Criação de um Data Lake: Após a coleta, os dados brutos foram armazenados em um Data Lake fictício. Construí uma pipeline visando minimizar erros e garantir que as informações fossem salvas de maneira eficiente. Essa etapa é crucial, pois permite a centralização dos dados em seu formato original.

Processamento de Dados: Em seguida, utilizei SQL para limpar e organizar os dados coletados. Essa fase incluiu a remoção de duplicatas, o tratamento de valores ausentes e a transformação dos dados em formatos apropriados. O objetivo foi preparar essas informações para serem inseridas em um Data Warehouse (DW), onde estarão estruturadas de forma a facilitar análises futuras.

Análise e Visualização: Após a organização dos dados, estou planejando utilizar ferramentas de visualização, como Tableau, para criar dashboards interativos. Isso permitirá uma análise mais simples e de fácil compreensão.

🔧 Tecnologias utilizadas:

Pandas
SQLAlchemy
dotenv
Render
DBeaver

🚀 Próximos passos:

Possível integração com Apache Airflow para automatizar o processo de ELT.

Migração para Apache Spark para aumentar a eficiência no processamento de dados.

Criação de visualizações no Tableau para apresentar insights de forma mais clara e limpa.

Qualquer dúvida ou sugestão, sinta-se à vontade!

![Pipeline](https://github.com/user-attachments/assets/9ca482c3-2908-4da0-ad6c-110cd38603e2)
![Print_DW](https://github.com/user-attachments/assets/b5fe9f57-92bb-4b69-90d0-6402dcc9038c)
![Print_DL](https://github.com/user-attachments/assets/57734e9b-12b8-477d-83a0-2880d934d62c)
