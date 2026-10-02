<a href="https://github.com/EEw3n3">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/dark_mode.svg">
    <img alt="Ervin Ubinin — software developer: Python, backend, web scraping, DevOps" src="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/light_mode.svg">
  </picture>
</a>

## Ervin Ubinin

**Software Developer** · Riga, Latvia

I build backend services, data pipelines and automation, mostly in Python. I take a service the whole way:
collecting data from the web, storing it in PostgreSQL, serving it through a REST API, and running it in Docker
on a Linux server with automated deployments.

<img src="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/divider.svg" width="100%" height="6" alt="">

### What I work on

| Area | Details |
|:--|:--|
| **Backend** | REST APIs with FastAPI and Pydantic · async SQLAlchemy / SQLModel · PostgreSQL schema design and Alembic migrations · Redis job queues · JWT authentication · Telegram and e-mail notifications |
| **Web scraping & data** | Playwright (Chrome) and curl_cffi · reading the JSON that sites embed in their pages · intercepting XHR/Fetch requests and reverse-engineering site APIs · normalising and matching the same product across stores · validation and de-duplication |
| **DevOps** | Docker and Docker Compose · Linux (Ubuntu) servers · Caddy reverse proxy with automatic HTTPS · GitHub Actions CI/CD |
| **AI integration** | Anthropic Claude Opus 5.5, Sonnet 5.5 and Fable 5.1 · OpenAI GPT-6 Astra · Google Gemini Flash and Pro models — through their APIs, for CSS-selector generation that repairs scrapers, data extraction, and chat assistants that answer from a database |
| **Frontend** | React and TypeScript with Tailwind CSS — dashboards for my own services |

<img src="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/divider.svg" width="100%" height="6" alt="">

### Tech stack

**Languages & backend**<br>
![Python](https://img.shields.io/badge/Python-1f2328?style=for-the-badge&logo=python&logoColor=FFD43B)
![TypeScript](https://img.shields.io/badge/TypeScript-1f2328?style=for-the-badge&logo=typescript&logoColor=3178C6)
![SQL](https://img.shields.io/badge/SQL-1f2328?style=for-the-badge&logo=sqlite&logoColor=74C0FC)
![FastAPI](https://img.shields.io/badge/FastAPI-1f2328?style=for-the-badge&logo=fastapi&logoColor=009688)
![Pydantic](https://img.shields.io/badge/Pydantic-1f2328?style=for-the-badge&logo=pydantic&logoColor=E92063)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1f2328?style=for-the-badge&logo=sqlalchemy&logoColor=D71F00)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-1f2328?style=for-the-badge&logo=postgresql&logoColor=4169E1)
![Redis](https://img.shields.io/badge/Redis-1f2328?style=for-the-badge&logo=redis&logoColor=DC382D)

**Web scraping, data & APIs**<br>
![Playwright](https://img.shields.io/badge/Playwright-1f2328?style=for-the-badge&logo=googlechrome&logoColor=2EAD33)
![curl_cffi](https://img.shields.io/badge/curl__cffi-1f2328?style=for-the-badge&logo=curl&logoColor=white)
![XHR / Fetch interception](https://img.shields.io/badge/XHR%20%2F%20Fetch%20interception-1f2328?style=for-the-badge&logo=googlechrome&logoColor=4285F4)
![asyncio](https://img.shields.io/badge/asyncio-1f2328?style=for-the-badge&logo=python&logoColor=FFD43B)
![REST APIs](https://img.shields.io/badge/REST%20APIs-1f2328?style=for-the-badge&logo=openapiinitiative&logoColor=6BA539)
![Claude API](https://img.shields.io/badge/Claude%20API-1f2328?style=for-the-badge&logo=anthropic&logoColor=D97757)
![OpenAI API](https://img.shields.io/badge/OpenAI%20API-1f2328?style=for-the-badge&logo=openai&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini%20API-1f2328?style=for-the-badge&logo=googlegemini&logoColor=8E75B2)
![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-1f2328?style=for-the-badge&logo=telegram&logoColor=26A5E4)

**DevOps**<br>
![Docker](https://img.shields.io/badge/Docker-1f2328?style=for-the-badge&logo=docker&logoColor=2496ED)
![Linux](https://img.shields.io/badge/Linux-1f2328?style=for-the-badge&logo=linux&logoColor=FCC624)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-1f2328?style=for-the-badge&logo=githubactions&logoColor=2088FF)
![Git](https://img.shields.io/badge/Git-1f2328?style=for-the-badge&logo=git&logoColor=F05032)
![Bash](https://img.shields.io/badge/Bash-1f2328?style=for-the-badge&logo=gnubash&logoColor=4EAA25)
![Caddy](https://img.shields.io/badge/Caddy-1f2328?style=for-the-badge&logo=caddy&logoColor=1F88C0)
![DigitalOcean](https://img.shields.io/badge/DigitalOcean-1f2328?style=for-the-badge&logo=digitalocean&logoColor=0080FF)

**Frontend**<br>
![React](https://img.shields.io/badge/React-1f2328?style=for-the-badge&logo=react&logoColor=61DAFB)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-1f2328?style=for-the-badge&logo=tailwindcss&logoColor=06B6D4)

<img src="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/divider.svg" width="100%" height="6" alt="">

### Main project

**MarketPulse** — price monitoring for the Latvian perfume market. It collects the catalogues of
Douglas, Notino, Makeup.lv and 220.lv, recognises the same product in every store, records each price change
and notifies users when a price drops.

- A scraping strategy per store: the shop's REST API, JSON embedded in the page, intercepted XHR requests, HTML
- 18,800 product variants tracked; 1,400 products matched across stores
- Price history, Telegram and e-mail alerts, analytics, XLSX/PDF export, AI chat over the catalogue
- FastAPI · PostgreSQL · Redis · Playwright · React · Docker Compose · Caddy · GitHub Actions
- 47 registered users

*Public repository coming soon.*

<img src="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/divider.svg" width="100%" height="6" alt="">

### Education

**Rīgas Valsts tehnikums** — Programming, graduated 2026. Qualification project: MarketPulse.

<img src="https://raw.githubusercontent.com/EEw3n3/EEw3n3/main/divider.svg" width="100%" height="6" alt="">

### Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-1f2328?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](https://www.linkedin.com/in/erv%C4%ABns-ubi%C5%86ins-4099653a3/)
[![Email](https://img.shields.io/badge/ervinubinin1%40gmail.com-1f2328?style=for-the-badge&logo=gmail&logoColor=EA4335)](mailto:ervinubinin1@gmail.com)

<sub>The card at the top is drawn by <a href="generate_card.py">a Python script</a> and refreshed every day by GitHub Actions.</sub>
