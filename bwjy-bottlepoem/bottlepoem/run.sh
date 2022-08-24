docker build -t bottlepoem .
docker run -d -it --restart=always --name bottlesekai -p 8011:80 bottlepoem