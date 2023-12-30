const environment = {
  name: process.env.NAME || "API geoserver REST",
  pathBase: process.env.PATHBASE || "",
  port: process.env.PORT || 3001,
  authentication: {
    jwtSecret: process.env.JWT_SECRET || "KeyOauthJwt",
    jwtSession: { session: false },
    enableHTTPS: process.env.ENABLE_HTTPS || false,
    certificate: process.env.CERT_FILE || "",
    key: process.env.CERT_KEY_FILE || "",
  },
  geoserver: {
    url: process.env.URL_GEOSERVER || "http://localhost:8001/geoserver",
    user: process.env.USER_GEOSERVER || "admin",
    password: process.env.PASS_GEOSERVER || "1QmjuFsYakDrDlkXt7LS",
  },
};

export default environment;
