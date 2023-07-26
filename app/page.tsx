"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch("/api/data");
      const json = await res.json();
      setData(json);
    };
    fetchData();
  }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  return <h1>{data.yt_title}</h1>;
}
