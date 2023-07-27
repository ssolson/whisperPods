"use client";
import { useState, useEffect } from "react";

export default function EpisodePage({
  params,
}: {
  params: { ep_number: string };
}) {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const episodeNumber = parseInt(params.ep_number, 10);
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

  return (
    <div>
      <h1>Episode Page: {params.ep_number} </h1>

      <div>
        <h1>{data.episode_number}</h1>
        <h2>{data.episode_title}</h2>
        <h3>{data.release_date}</h3>

        {data.episode_data &&
          data.episode_data.map((item, index) => (
            <div key={index} style={{ marginBottom: "20px" }}>
              <h1>{item.story} </h1>
              <p>{item.summary}</p>
            </div>
          ))}
      </div>
    </div>
  );
}
