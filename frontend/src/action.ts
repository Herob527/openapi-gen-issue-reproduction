import { AudioApi } from "./types/generated/api";

const api = new AudioApi(
  {
    isJsonMime: (mime: string) => mime === "application/json",
  },
  "http://localhost:8000",
);

export const getData = async () => {
  const { data } = await api.indexAudiosPost();
  const test = data.files;
  console.log(test);
};
