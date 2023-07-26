import { NextResponse } from "next/server";
import { getClientAndDb } from "../mongo/db";

export async function GET() {
  try {
    const { client, db } = await getClientAndDb();
    const collection = db.collection("thedailygwei");
    const data = await collection.findOne({});

    return NextResponse.json(data);
  } catch (error) {
    // Handle error
    console.error(error);
  }
}

// // pages/api/data.js
// import nextConnect from "next-connect";
// import { getClientAndDb } from "../mongo/db";

// const handler = nextConnect();

// handler.use(async (req, res, next) => {
//   try {
//     const { client, db } = await getClientAndDb();
//     req.client = client;
//     req.db = db;
//     next();
//   } catch (error) {
//     res.status(500).json({ error: error.message });
//   }
// });

// handler.get(async (req, res) => {
//   try {
//     const collection = req.db.collection("thedailygwei");
//     const data = await collection.findOne({}).toArray();
//     res.status(200).json(data);
//   } catch (error) {
//     res.status(500).json({ error: error.message });
//   }
// });

// export default handler;

// import { NextResponse } from "next/server";

// const DATA_SOURCE_URL = "https://jsonplaceholder.typicode.com/todos";

// export async function GET() {
//   const response = await fetch(DATA_SOURCE_URL);
//   const data = await response.json();
//   return NextResponse.json(data);
// }
