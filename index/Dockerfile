FROM node:12.2.0-alpine as build

WORKDIR /index

ENV PATH /index/node_modules/.bin:$PATH

COPY . /index
RUN npm run build

#Running server
FROM nginx:1.16.0-alpine
COPY --from=build /index/dist /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]