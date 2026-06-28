import axios from "axios";

const api = axios.create({
    baseURL: "https://seo-analyzer-production-5591.up.railway.app/api",
    timeout: 60000
});

export default api;