"use client";
import { useState, useEffect } from "react";
import Link from "next/link";

export default function Home() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const episodeNumber = 624;
      const res = await fetch(`/api/all-episodes`);
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
      <h1>All Episodes</h1>
      {data.map((episode, index) => (
        <div key={index} style={{ marginBottom: "20px" }}>
          <p> {episode.release_date}</p>

          <h2>
            <Link
              style={{ color: "blue" }}
              href={`/episode/${episode.episode_number}`}
            >
              {episode.episode_number}
            </Link>
            {" - "}
            {episode.episode_title}
          </h2>
        </div>
      ))}
    </div>
  );
}
