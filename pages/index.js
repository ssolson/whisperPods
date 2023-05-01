import { useEffect, useState } from "react";
import DataTable from "./DataTable";

export default function Home() {
  const [data, setData] = useState([]);
  const [currentTranscript, setCurrentTranscript] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch("/api/data");
        if (!res.ok) {
          const error = await res.json();
          throw new Error(error.error);
        }
        const data = await res.json();
        console.log("Data fetched:", data);
        setData(data);
      } catch (error) {
        console.error("Error fetching data:", error.message);
      }
    }

    fetchData();
  }, []);

  const handleClick = (index) => {
    console.log(index);
    console.log(data[0]["transcript"]["text"]);
  };

  return (
    <div className="grid-cols auto grid h-screen w-full bg-gray-900">
      <div className="mx-auto my-auto h-1/4 w-1/2">
        <h1 className="text-3xl text-white">Episodes</h1>
        <br></br>
        <div className="flex flex-wrap">
          {data.map((index) => (
            <div key={index} className="flex flex-col">
              {index["Episode Name"].map((episode, index) => (
                <div
                  key={index}
                  className="text-white"
                  onClick={() => handleClick(index)}
                >
                  {episode}
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
      {/* <div className="bg-black">{data[0]["transcript"][currentTranscript]}</div> */}
    </div>
  );
}
