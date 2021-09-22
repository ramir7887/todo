import axios from "axios";

export function httpClient() {
	const headers = {
		"Content-Type": "application/json"
	}

	return axios.create({
		headers: headers,
		baseURL: "https://infinite-tundra-82240.herokuapp.com/api"
		//baseURL: "http://localhost:8000/api"
	})
}