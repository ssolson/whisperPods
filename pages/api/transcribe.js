import { exec } from "child_process";

function runPythonScript(filename, model) {
  console.log(
    `runPythonScript called with filename: ${filename} and model: ${model}`
  );
  return new Promise((resolve, reject) => {
    const command = `python python-backend\\whisperpod\\transcribe\\transcribePod.py "${filename}" "${model}"`;
    console.log(`Executing command: ${command}`);
    exec(command, (error, stdout, stderr) => {
      console.log("Exec callback:", { error, stdout, stderr });
      if (error) {
        reject(error);
      } else {
        try {
          const result = JSON.parse(stdout);
          resolve(result);
        } catch (err) {
          reject(new Error("Failed to parse Python script output"));
        }
      }
    });
  });
}

export default async function handler(req, res) {
  const { method } = req;

  switch (method) {
    case "POST":
      const { filename, model } = req.body;

      try {
        const result = await runPythonScript(filename, model);
        res.status(200).json(result);
      } catch (error) {
        console.error("Error in handler:", error);
        res.status(500).json({ error: error.message });
      }
      break;
    default:
      res.setHeader("Allow", ["POST"]);
      res.status(405).end(`Method ${method} Not Allowed`);
  }
}
