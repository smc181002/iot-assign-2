import express, { Express, Request, Response } from "express";
import {sequelizeConnection} from './db/config';

import Feed from './routes/feed.route';

const app: Express = express();
const port = process.env.PORT || 4000;

app.use("/api/v1/feed/", Feed);

app.get('/', (_: Request, res: Response) => {
    res.json({"message": "Hello there"});
});

app.listen(port, async () => {
    try {
        await sequelizeConnection.authenticate()
        await sequelizeConnection.sync();
        console.log("🗄️ Database connected");
    } catch (e) {
        console.error("❌🗄️ Unable to connect to database");
        throw e;
        return 1;
    }

    console.log(`🚀 server running on: 🌐http://localhost:${port}`)
})
