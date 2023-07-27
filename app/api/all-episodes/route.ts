// file: /pages/api/all-episodes.ts

import { NextResponse } from "next/server";
import { getClientAndDb } from "../mongo/db";

export async function GET() {
  try {
    const { db } = await getClientAndDb();
    const collection = db.collection("thedailygweiRecap");

    // Fetch all documents from the collection
    const data = await collection.find().toArray();
    // console.log("data", data);

    // Return the data in a standard response format
    return NextResponse.json({ status: 200, message: "Success", data: data });
  } catch (error) {
    console.error(error);

    // Return a 500 Internal Server Error response with the error message
    return NextResponse.error({ status: 500, message: error.message });
  }
}
