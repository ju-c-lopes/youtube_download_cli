
# YouTube Download CLI with Docker

This application download videos or an entire playlist from Youtube running through a docker container

---
<div style="display: flex; flex-direction: row; justify-content: space-around; align-items: center">
<img height="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" />
<img height="40" src="https://i.imgur.com/gvC3o3k.png" />
<img height="80" src="https://i.imgur.com/i6dBYRb.png" />
</div>

---

_OBS_: You'll need to get docker installed in your machine. Just in case you don't, you can follow the instruction on [Docker Docs](https://docs.docker.com/engine/install/).

### Instructions

1. Clone this repository in a desired folder in your machine following this command ```git clone https://github.com/ju-c-lopes/youtube_download_cli·git .```

2. Run this command ```docker build -t youtube_download .```

3. After the build had been finished, it's important to run this command how it's been showing. Run ```docker run -it -v $(pwd)/Downloads:/app/Downloads youtube_download```

4. You'll be asked which type operation you want to do, so choose between *download a single video* or if you want to *dowwnload an entire playlist*

5. Finished downloads will be saved at the _**Download Folder**_

6. Enjoy it
