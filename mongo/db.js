import { MongoClient } from "mongodb";

const MONGO_URI = process.env.MONGO_URI;

const connectToDB = async () => {
  const client = new MongoClient(MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  if (!client.isConnected()) await client.connect();

  return {
    client,
    db: client.db("whisperPods"),
  };
};

export default connectToDB;
