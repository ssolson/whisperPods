function DataTable({ data }) {
  const headers = [
    "Date",
    "Episode Name",
    "Podcast Name",
    "Podcast Number",
    "Subtitle",
    "Filename",
  ];

  return (
    <table>
      <thead>
        <tr>
          {headers.map((header) => (
            <th key={header}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((_, index) => (
          <tr key={index}>
            <td>{data.Date[index]}</td>
            <td>{data["Episode Name"][index]}</td>
            <td>{data["Podcast Name"][index]}</td>
            <td>{data["Podcast Number"][index]}</td>
            <td>{data.Subtitle[index]}</td>
            <td>{data.filename[index]}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DataTable;
