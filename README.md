**small url-preview docker project with vulnerabilities scanning via github actions**

On every new push to the main branch:
1. the Docker container gets built
2. the image is pushed to the ghcr
3. docker Scout is run to scan the image for critical and high vulnerabilities
