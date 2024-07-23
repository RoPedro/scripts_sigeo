<a name="readme-top">En | Pt-br</a>

<br />
<div align="center">
<h3 align="center">General scripts repository | Repositório de scripts gerais</h3>
  <p align="center">
    This repository was created to organize and share some general scripts using arcgis.gis and arcpy libaries
  </p>
  <p>
    Esse repositório tem como objetivo organizar e compartilhar scripts de uso diverso utilizando as bibliotecas arcgis.gis e arcpy
  </p>
  <p><a href="https://github.com/SIGeo-Niteroi/scripts/issues">Report Bug</a></p>
</div>

<details>
  <summary>Table of contents | Súmario</summary>
  <ol>
    <li>
      <a href="#about-the-repository--sobre-o-repositório">About The Repository | Sobre O Repositório</a>
      <ul>
        <li><a href="#built-with--desenvolvido-com">Built With | Desenvolvido Com</a></li>
      </ul>
    </li>
    <li>
      <a href="#scripts">Scripts</a>
      <ul>
        <li><a href="#arcgis-pro">ArcGIS Pro</a></li>
        <li><a href="#arcgis-online">ArcGIS Online</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started | Inicializando</a>
      <ul>
        <li><a href="#prerequisites--pré-requisitos">Prerequisites | Pré-requisitos</a></li>
        <li><a href="#installation--instalação">Installation | Instalação</a></li>
      </ul>
    </li>
    <li><a href="#usage--uso">Usage | Uso</a></li>
    <li><a href="#-contributing--contribuindo">Contributing | Contribuindo</a></li>
    <li><a href="#contact--contato">Contact | Contato</a></li>
    <li><a href="#contributors--contribuidores">Contributors | Contribuidores</a></li>
  </ol>
</details>

## About The Repository | Sobre O Repositório

Welcome! This is a repository created by SIGEO from Niterói city hall to organize and share some of our geoprocessing scripts. Here you can find some general scripts using arcgis.gis and arcpy libraries with spatial data.

<p>Bem vindo(a)! Esse é um repositório criado pelo SIGEO da prefeitura de Niterói para organizar e compartilhar alguns de nossos scripts de geoprocessamento. Aqui você encontra scripts de uso diverso utilizando as bibliotecas arcgis.gis e arcpy com dados espaciais.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With | Desenvolvido Com

[![Python]][Python-url] ![env] ![Arcgis]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Scripts

### ArcGIS Pro

  <h5>Publicação camadas através do ArcGIS Pro</h5>
  
  :desktop_computer: ```publicar_camadas_arcgispro```
  
   <p>Código para publicar camadas de um geodatabase no ArcGIS Pro como camadas hospedadas</p>

### ArcGIS Online

  <h5>Mudança de visibilidade de camada no webmap</h5>
  
  :desktop_computer: ```mudança_visibilidade_webmap```
  
  <p>Código para deixar a visibilidade das camadas de um webmap desligada</p> 
  
  <h5>Mudança de visibilidade de camada no webmap</h5>
  
  :desktop_computer: ```transferencia_simbologia```
  
  <p>Código para transferir uma simbologia de uma camada em um webmap para uma camada hospedada</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

First, install the dependencies needed to run this project

<p>Primeiro, instale as dependencias necessárias para rodar o projeto</p>

### Prerequisites | Pré-requisitos

- Python -> https://www.python.org/
- Arcpy -> https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm
- Arcgis.gis -> https://developers.arcgis.com/python/

### Installation | Instalação

1. Clone the repo | Clone o repositório
   ```sh
   git clone https://github.com/SIGeo-Niteroi/scripts.git
   ```

2. Install Libraries | Instale as bibliotecas

3. Create a .env local file based on the .env.example file | Crie um arquivo local .env baseado no arquivo .env.example
   *When necessary | quando necessário* 

4. Start the application | Rode o script
    ```sh
    ptyhon script.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage | Uso

Will be listed here the code's demo | Será inserido aqui uma demo do uso dos códigos

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing | Contribuindo
Contributions are **greatly appreciated**! | Contribuições são **sempre bem vindas**!

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also open an issue with the tag "enhancement".
<p>Se você possuir alguma sugestão que possa tornar esse projeto melhor, por favor fork esse repositório e crie um pull request. Você pode também abrir um issue com a tag "enhancement".</p>

1. Fork the Project | Fork o Projeto
2. Create your Feature Branch | Crie sua  Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes | Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch | Push para sua Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request | Abra um Pull Request

Thanks! Obrigado! 😄

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact | Contato

Sistema de Gestão de Geoinformação - [Portal SIGeo](https://www.sigeo.niteroi.rj.gov.br/) - atendimento@sigeo.niteroi.rj.gov.br

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributors | Contribuidores

<img src="https://contrib.rocks/image?repo=SIGeo-Niteroi/scripts&anon=0&columns=20&max=100" alt="Lista de contribuidores"/>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Arcgis]: https://img.shields.io/badge/ArcGIS-2C7AC3.svg?style=for-the-badge&logo=ArcGIS&logoColor=white
[env]: https://img.shields.io/badge/.ENV-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=black
