"use client"

import {useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import useSWR from "swr";
import Image from "next/image";

const HomePage = () => {
  const [page, setPage] = useState(1);
  const itemsPerPage = 24;

  const fetchData = async (url: string) => {
    try {
      const response = await axios.get(url, {
        params: {
          page: page,
          items_per_page: itemsPerPage,
        },
      });
      const data = response.data ? response.data : [];
      return data;
    } catch (error: any) {
      toast.error("Something went wrong.");
      throw new Error(error);
    }
  };

  const { data, error, isLoading } = useSWR(
    `http://127.0.0.1:8080/api/data`,
    fetchData
  );

  if (error) {
    console.log(error)
    return (
      <div>
        Got unexpected error
      </div>
    );
  }
  // console.log(flats)

  return (
    <main className="bg-gray-900 flex w-full h-fit flex-col items-center">
      <div className="z-10 max-w-6xl mx-auto px-4 sm:px-6">
        {/* Hero content */}
        <div className="pt-12 md:pt-16">
          {/* Section header */}
          <div className="text-center">
            <h1
              className="text-5xl md:text-6xl font-extrabold leading-tighter tracking-tighter mb-4 dark:text-white text-black"
              data-aos="zoom-y-out"
            >
              Best flats in
              <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-red-400">
                <br />
                Czechia
              </span>
            </h1>
            <div className="max-w-3xl mx-auto">
              <p
                className="text-xl text-gray-600 mb-8"
                data-aos="zoom-y-out"
                data-aos-delay="150"
              >
                Discover best flats on out website!
              </p>
              <div
                className="max-w-xs mx-auto sm:max-w-none sm:flex sm:justify-center"
                data-aos="zoom-y-out"
                data-aos-delay="300"
              >
              </div>
            </div>
          </div>
        </div>
      </div>
      {error && (
        <div>
          Couldnt load data
        </div>
      )}
      {isLoading ? (
        <div>Loading</div>
      ) : (
        <>
          <div className="mt-8 mb-32 grid gap-8 lg:mb-0 md:grid-cols-2 lg:grid-cols-3">
            {data.map((item: any, index: number) => (
              <div className="flex bg-black/40 flex-col w-fit h-fit p-3 rounded-md cursor-pointer transition hover:scale-105" key={index}>
                {/* IMAGE AREA */}
                <Image 
                  objectFit="cover"
                  width={400}
                  height={300}
                  alt={item[0]}
                  src={item[1]}
                  className="rounded-md"
                />
                {/* FOOTER AREA */}
                <p className="text-white py-4">
                  {item[0]}
                </p>
              </div>
            ))}
          </div>
          <button
            onClick={() => setPage((prevPage) => Math.max(prevPage - 1, 1))}
          >
            Previous
          </button>
          <button onClick={() => setPage((prevPage) => prevPage + 1)}>
            Next
          </button>
        </>
      )}
    </main>
  );
};

export default HomePage;
