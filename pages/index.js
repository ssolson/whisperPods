import { useEffect, useState } from "react";
import DataTable from "./DataTable";

export default function Home() {
  const [data, setData] = useState([]);
  const [selectedPodcast, setSelectedPodcast] = useState("");
  const [currentTranscript, setCurrentTranscript] = useState({
    transcript: null,
    execution_time: null,
  });
  const [transcribing, setTranscribing] = useState(false);

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

  const handleClick = () => {
    console.log(data[0]["Episode Name"]);
  };

  async function transcribeAudio(filename, model) {
    setTranscribing(true); // Start transcribing
    const response = await fetch("/api/transcribe", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        filename: filename,
        model: model,
      }),
    });

    if (!response.ok) {
      const message = `An error occurred: ${response.statusText}`;
      throw new Error(message);
    }

    const data = await response.json();
    setCurrentTranscript({
      transcript: data.transcript,
      execution_time: data.execution_time,
    });

    setTranscribing(false); // End transcribing
  }

  return (
    <div className="grid-cols auto grid h-screen w-full bg-gray-900 text-white">
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
      <div className="flex h-12 w-full justify-center">
        <button
          className="mx-auto rounded-lg border border-white bg-orange-300 bg-opacity-20 p-2 transition-all duration-300 hover:bg-orange-600 hover:bg-opacity-80"
          onClick={() => {
            transcribeAudio(
              `C:\\Users\\fuck\\Desktop\\cwcode\\whisper.pods\\whisperPods\\python-backend\\podcast\\thedailygwei\\2023\\2023.04.26 EthStaker Knowledge Base, Market chat and more - The Daily Gwei Refuel #574 - Ethereum Updates.mp3`,
              "tiny.en"
            );
          }}
        >
          Transcribe
        </button>
      </div>
      <div className="h-full overflow-scroll overflow-y-auto bg-black p-14">
        <div className={transcribing ? "loading-text " : ""}>
          {currentTranscript.transcript ? (
            <div className="flex flex-col justify-center">
              <div className="text-yellow-400">
                Execution time: {Math.floor(currentTranscript.execution_time)}{" "}
                seconds.
              </div>
              <br></br>
              <div>{currentTranscript.transcript.text}</div>
            </div>
          ) : transcribing ? (
            "Transcribing. This could take a while..."
          ) : (
            ""
          )}
        </div>
      </div>
    </div>
  );
}
