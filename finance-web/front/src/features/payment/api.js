import axios from "axios";
const ENDPOINT = process.env.REACT_APP_ENDPOINT;
export const API_URL = String(ENDPOINT);

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-type": "application/json"
  }
});

export default class ApiService{
  static saveStripeInfo(data={}){
    return api.post(`${API_URL}api/save-stripe-info/`, data)
  }
}