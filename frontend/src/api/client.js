import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/simulation';

export const initSimulation = async (bodies) => {
    const response = await axios.post(`${API_BASE_URL}/init`, { bodies });
    return response.data;
};

export const stepSimulation = async (dt, steps = 1) => {
    const response = await axios.post(`${API_BASE_URL}/step`, { dt, steps });
    return response.data;
};

export const getState = async () => {
    const response = await axios.get(`${API_BASE_URL}/state`);
    return response.data;
};
