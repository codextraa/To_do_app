const HTTPS = process.env.HTTPS == "true";

export class ApiClient {
  constructor(baseURL) {
    this.baseURL = baseURL;
  }

  async request(endpoint, method, data) {
    const url = `${this.baseURL}${endpoint}`;
    const options = {
      method: method,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(HTTPS && { Referer: process.env.NEXT_PUBLIC_BASE_HTTPS_URL }),
      },
      credentials: "include",
    };

    if (data) {
      options.body = JSON.stringify(data);
    }

    try {
      const response = await fetch(url, options);

      if (response.status >= 400) {
        console.log("Some Error Occured");
        return null;
      }

      if (response.status == 204) {
        return null;
      }
      const responseData = await response.json();
      return responseData;
    } catch (error) {
      console.error("Fetch error:", error);
      throw error;
    }
  }

  async get(endpoint) {
    return await this.request(endpoint, "GET", null);
  }

  async post(endpoint, data) {
    return await this.request(endpoint, "POST", data);
  }

  async patch(endpoint, data) {
    return await this.request(endpoint, "PATCH", data);
  }

  async put(endpoint, data) {
    return await this.request(endpoint, "PUT", data);
  }

  async delete(endpoint, data = null) {
    return await this.request(endpoint, "DELETE", data);
  }
}
