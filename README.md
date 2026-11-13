```
 _   _____   __   ____  ___  ___   _  ________                
| | / / _ | / /  / __ \/ _ \/ _ | / |/ /_  __/__________  ____
| |/ / __ |/ /__/ /_/ / , _/ __ |/    / / / /___/ __/ _ \/ __/
|___/_/ |_/____/\____/_/|_/_/ |_/_/|_/ /_/     /_/ / .__/\__/ 
                                                  /_/         
```
[![Stars][stars-shield]][stars-url]
[![Releases][releases-shield]][releases-url]
[![Language][language-shield]][language-url]
[![License][license-shield]][license-url]

> **This is a fork of [colinhartigan/valorant-rpc](https://github.com/colinhartigan/valorant-rpc).**
> All credit for the original project goes to Colin Hartigan. This fork fixes the rich presence so it works with current versions of VALORANT.

> **Join the [Discord Server](https://discord.gg/Q4c98dKD82) to get help with any issues running the program or to report it needing a fix**

  <ol>  
    <li><a href="#about">About</a></li>
    <li><a href="#whats-fixed">What's Fixed</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#support">Support</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
  </ol>
 
 
## About

 Valorant RPC (Rich Presence) allows you to show in-game details such as the current score in your Discord Profile! Additional features include showing current map, agent, idle status, etc.

 
 <a>
    <img src="assets/Demo1.png" alt="Demo" width="205" height="112">
    <img src="assets/Demo2.png" alt="Demo" width="205" height="112">

 </a>

 
 
## What's Fixed

 The original project stopped working after Riot changed how VALORANT reports player presence, and newer maps, agents and ranks had no images. These are all the fixes made in this fork:

### Presence detection
 - **Nested presence data** – Riot moved most presence fields (`sessionLoopState`, `partySize`, `queueId`, match/party info, etc.) out of the top level and into nested objects: `matchPresenceData`, `partyPresenceData`, `playerPresenceData` and `premierPresenceData`. The app was reading the old locations, so it could no longer tell whether you were in the menus, in queue or in a match.
 - **New client wrapper** – added [`src/utilities/client.py`](src/utilities/client.py), which extends `valclient.Client` and copies those nested fields back to the top level whenever presence is fetched. Existing top-level values are never overwritten, so the rest of the app works without changes.
 - **Startup uses the patched client** – [`src/startup.py`](src/startup.py) now creates the patched `Client` instead of `valclient.Client`.

### Images
 - **Map images** – maps used hardcoded Discord asset keys like `splash_ascent`, which don't exist for newer maps. Map images are now loaded from valorant-api (`listViewIconTall`, falling back to `splash`, then `listViewIcon`), with the VALORANT logo as a last resort.
 - **Agent images** – agents used asset keys like `agent_jett`, so newer agents had no picture. Agent icons are now loaded from valorant-api (`displayIcon`).
 - **Rank images** – rank icons are now loaded from valorant-api (`largeIcon`, falling back to `smallIcon`) instead of `rank_<id>` asset keys.
 - **The Range and custom game setup** – both presences now use the same map image lookup instead of hardcoded `splash_range` / `splash_<map>` keys.
 - The old Discord asset keys are still used as a fallback if valorant-api doesn't return an image.

### Game modes
 - **Premier** – added Premier to the list of game modes so it displays correctly.

### Other
 - **Startup banner** – the ASCII banner in `main.py` used an f-string full of backslashes, which caused invalid escape sequence warnings on newer Python versions. It's now a raw string.
 - **`.gitignore`** – added `.venv/`.
 - **Fork links** – the GitHub button, update checker, tray icon download and join-link redirect now point to this fork instead of the original repo.

 
 
## Installation

 - Download the latest [release](https://github.com/seekwarmthwithchrist/valorant-rpc/releases/latest/download/valorant-rpc.exe) and run it.

 
 
## Usage

 - Run the program instead of launching VALORANT
     - If VALORANT is not running, the program will launch it for you
 - If VALORANT is already running, launch the program and the presence will start


 
## Support

 Found a bug? [Open an issue](https://github.com/seekwarmthwithchrist/valorant-rpc/issues) on this fork.

 Please don't report issues with this fork to the original project.
 
 
 
## Credits

 - **[Colin Hartigan](https://github.com/colinhartigan)** – original author of [valorant-rpc](https://github.com/colinhartigan/valorant-rpc) and [valclient](https://github.com/colinhartigan/valclient)
 - **[seekwarmthwithchrist](https://github.com/seekwarmthwithchrist)** – fixes for current VALORANT versions
 
 
 
## Disclaimer 

 This project is not affiliated with Riot Games or any of its employees and therefore does not reflect the views of said parties.
 
 Riot Games does not endorse or sponsor this project. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
 
 
 
[license-shield]: https://img.shields.io/github/license/seekwarmthwithchrist/valorant-rpc?style=for-the-badge
[license-url]: https://github.com/seekwarmthwithchrist/valorant-rpc/blob/v3/LICENSE.txt

[stars-shield]: https://img.shields.io/github/stars/seekwarmthwithchrist/valorant-rpc?logo=github&style=for-the-badge
[stars-url]: https://github.com/seekwarmthwithchrist/valorant-rpc/stargazers

[releases-shield]: https://img.shields.io/github/downloads/seekwarmthwithchrist/valorant-rpc/total?style=for-the-badge
[releases-url]: https://github.com/seekwarmthwithchrist/valorant-rpc/releases

[language-shield]: https://img.shields.io/github/languages/top/seekwarmthwithchrist/valorant-rpc?logo=python&logoColor=yellow&style=for-the-badge
[language-url]: https://www.python.org/
