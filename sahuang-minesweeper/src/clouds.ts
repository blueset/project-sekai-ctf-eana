export function animateCloud() {
  const clouds: HTMLElement[] = [];
  debugger;

  const article = document.querySelector("article.title")!;

  for (let i = 0; i < 20; i++) {
    const cloud = document.createElement("span");
    cloud.innerText = "cloud";
    cloud.className = "cloud";
    const articleBdcr = article.getBoundingClientRect();
    const cloudBdcr = cloud.getBoundingClientRect();
    cloud.dataset.left = `${Math.random() * articleBdcr.width}`;
    cloud.dataset.top = `${
      Math.random() * (articleBdcr.height - cloudBdcr.height)
    }`;
    article.appendChild(cloud);
    clouds.push(cloud);
  }

  const speed = 0.01;
  const deviate = 0.001;
  let lastFrame = -1;

  let animating = true;

  function animate(time: number) {
    const delta = lastFrame < 0 ? 0 : time - lastFrame;
    lastFrame = time;
    const articleBdcr = article.getBoundingClientRect();
    for (let i = 0; i < clouds.length; i++) {
      const cloud = clouds[i];
      const cloudBdcr = cloud.getBoundingClientRect();
      cloud.dataset.left = `${
        parseFloat(cloud.dataset.left!) - delta * (speed + deviate * i)
      }`;
      if (cloudBdcr.right < 0) {
        cloud.dataset.left = `${articleBdcr.right}`;
        cloud.dataset.top = `${
          Math.random() * (articleBdcr.height - cloudBdcr.height)
        }`;
      }
      cloud.style.transform = `translate(${cloud.dataset.left}px, ${cloud.dataset.top}px)`;
    }
    
    if (animating) requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);

  return () => { 
    animating = false;
  }
}
