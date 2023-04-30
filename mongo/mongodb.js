// mongo/mongodb.js
import { MongoClient } from "mongodb";
require("dotenv").config({ path: "./mongo/config.env" });

const uri = process.env.ATLAS_URI;
const options = {
  useNewUrlParser: true,
  useUnifiedTopology: true,
};

let client;
let clientPromise;

if (!process.env.ATLAS_URI) {
  throw new Error("Please define the ATLAS_URI environment variable");
}

if (process.env.NODE_ENV === "development") {
  // In development mode, use a global variable to retain the MongoClient instance
  // across hot-reloads to avoid multiple MongoClient instances.
  if (!global.mongo) {
    global.mongo = { conn: null, promise: null };
  }
  client = global.mongo;
} else {
  // In production mode, use a module-scoped variable.
  client = {};
}

if (!client.promise) {
  client.promise = MongoClient.connect(uri, options).then((clientInstance) => {
    const db = clientInstance.db("whisperPods");
    return { client: clientInstance, db };
  });
}

const getClientAndDb = async () => {
  const { client: clientInstance, db } = await client.promise;
  return { client: clientInstance, db };
};

export { getClientAndDb };
