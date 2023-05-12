const { MongoClient, ServerApiVersion } = require("mongodb");
require("dotenv").config({ path: "./mongo/config.env" });
const uri = process.env.ATLAS_URI;

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    console.log("Connected to MongoDB!");

    // Specify the database and collection
    const db = client.db("whisperPods");
    const collection = db.collection("thedailygwei");

    // Find a single document
    const data = await collection.findOne({});
    console.log(data);
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);
