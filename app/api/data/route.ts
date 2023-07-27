import { NextResponse } from "next/server";
import { getClientAndDb } from "../mongo/db";

export async function GET(req) {
  try {
    const { client, db } = await getClientAndDb();
    const collection = db.collection("thedailygweiRecap");

    // Get query parameters for filtering (e.g., req.query.id)
    const query = req.query || {};
    console.log(query);

    // Fetch data from the collection based on query parameters
    const data = await collection.findOne(query);

    if (!data) {
      // If no data was found, return a 404 Not Found response
      return NextResponse.error({ status: 404, message: "Data not found" });
    }

    // Return the data in a standard response format
    return NextResponse.json({ status: 200, message: "Success", data: data });
  } catch (error) {
    console.error(error);

    // Return a 500 Internal Server Error response with the error message
    return NextResponse.error({ status: 500, message: error.message });
  }
}
