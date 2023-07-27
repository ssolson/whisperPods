"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const episodeNumber = 624; // replace with the actual episode number
      const res = await fetch(`/api/episode?episode_number=${episodeNumber}`);
      const json = await res.json();
      setData(json["data"]);
    };
    fetchData();
  }, []);

  if (!data) {
    return (
      <div>
        Loading... <br />
        <button
          onClick={async () => {
            const res = await fetch(`/api/episode?episode_number="624"}`);
            console.log(res);
          }}
        >
          Reload
        </button>
      </div>
    );
  }

  // console.log(data);
  // console.log(data.episode_number);

  return (
    <div>
      <h1>{data.episode_number}</h1>
      <h2>{data.item_title}</h2>
      <h3>{data.release_date}</h3>

      {data.episode_data &&
        data.episode_data.map((item, index) => (
          <div key={index} style={{ marginBottom: "20px" }}>
            <h1>{item.story} </h1>
            <p>{item.summary}</p>
          </div>
        ))}
    </div>
  );
}
