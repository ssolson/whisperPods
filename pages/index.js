import { useEffect, useState } from "react";
import DataTable from "./DataTable";
import { Select, Divider, Image } from "antd";

export default function Home() {
  const [data, setData] = useState([]);
  const [selectedPodcast, setSelectedPodcast] = useState("");
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

  const onChange = (value) => {
    setSelectedPodcast(value);
  };

  const onSearch = (value) => {
    console.log("search:", value);
  };

  const selectedPodcastData = data.find((item) => item._id === selectedPodcast);

  const latestEpisode = data[data.length - 1] || null;

  return (
    <div className="grid-cols auto grid h-full min-h-screen w-full bg-gray-900 text-white">
      <div className="flex w-full flex-col flex-wrap">
        {data.length > 1 ? (
          <div className="flex h-full w-full justify-between">
            <div className="mt-20 flex w-full flex-col flex-wrap">
              <div className="m-4 mx-auto flex flex-col justify-center border p-4 text-center">
                <p className="font-semibold">Total Episodes</p>
                <Divider className="my-2 bg-white" />
                <p className="text-3xl font-bold">{data.length}</p>
              </div>
              <Select
                className="mx-auto w-64"
                showSearch
                placeholder="Select an episode"
                optionFilterProp="children"
                onChange={onChange}
                onSearch={onSearch}
                filterOption={(input, option) =>
                  (option?.label ?? "")
                    .toLowerCase()
                    .includes(input.toLowerCase())
                }
                options={data.map((item) => ({
                  value: item._id,
                  label: item.item_title,
                }))}
              />
              <div className="mx-auto w-full p-12">
                {selectedPodcastData?.yt_transcript?.map((entry) => (
                  <div key={entry.start} className="w-full">
                    <p>{entry.text}</p>
                  </div>
                ))}
              </div>
            </div>
            <div className="h-full w-1/5 border text-center">
              <h1 className="p-4 pb-1 text-xl font-semibold">Latest Episode</h1>
              <p className="">
                {latestEpisode?.release_date?.substring(0, 10)}
              </p>
              <Divider className="mb-0 mt-2 bg-white" />
              <Image
                src={latestEpisode?.image_url}
                alt="Latest episode"
                className="w-full"
              />
              <div className="p-4 text-center">
                <p className="text-lg">{latestEpisode?.item_title}</p>
              </div>
            </div>
          </div>
        ) : (
          <div className="mx-auto mt-20 flex flex-col flex-wrap">
            loading...
          </div>
        )}
      </div>
    </div>
  );
}
