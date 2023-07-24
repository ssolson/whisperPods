// pages/api/data.js
import nextConnect from "next-connect";
import { getClientAndDb } from "../../mongo/mongodb";

const handler = nextConnect();

handler.use(async (req, res, next) => {
  try {
    const { client, db } = await getClientAndDb();
    req.client = client;
    req.db = db;
    next();
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

handler.get(async (req, res) => {
  try {
    const collection = req.db.collection("thedailygweiRecap");
    // const data = await collection.findOne({}).toArray();
    // const data = await collection.findOne({}).cursor().toArray();
    const data = await collection.findOne({});

    console.log(data["episode_data"]);

    // res.status(200).json(data);
    res.status(200).json(data["episode_data"]);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

export default handler;
