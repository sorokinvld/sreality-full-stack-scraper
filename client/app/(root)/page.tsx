"use client"

import {useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import useSWR from "swr";
import Image from "next/image";
import PreviousMap from "postcss/lib/previous-map";

const HomePage = () => {
  const [page, setPage] = useState(1);
  const itemsPerPage = 12;

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
  console.log(data)
  return (
    <main className="text-white flex w-full h-fit flex-col items-center mb-10">
      <div className="z-10 max-w-6xl mx-auto px-4 sm:px-6">
        {/* Hero content */}
        <div className="pt-12 md:pt-16">
          {/* Section header */}
          <div className="text-center">
            <h1
              className="text-5xl md:text-6xl font-extrabold leading-tighter tracking-tighter mb-4 dark:text-white text-black"
              data-aos="zoom-y-out"
            >
              Let's Find Your
              <span className="bg-clip-text text-transparent bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500">
                <br />
                Comfort House!
              </span>
            </h1>
            <div className="max-w-3xl mx-auto">
              <p
                className="text-xl text-gray-600 mb-8"
                data-aos="zoom-y-out"
                data-aos-delay="150"
              >
                Modern & Classic
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
      {error ? (
        <div className=" text-center" >
          Couldnt load data
        </div>
      ): (
        <>
          {isLoading ? (
            <div className="text-white text-center">Loading</div>
          ) : (
            <>
              <div className="mt-8 mb-32 grid gap-8 lg:mb-0 md:grid-cols-2 lg:grid-cols-3">
                {data.map((item: any, index: number) => (
                  <div className="relative flex flex-col items-center w-fit h-fit cursor-pointer transition" key={index}>
                    {/* IMAGE AREA */}
                    <Image 
                      objectFit="cover"
                      width={400}
                      height={300}
                      alt={item[0]}
                      src={item[1]}
                      className="rounded-2xl"
                    />
                    {/* FOOTER AREA */}
                    <p className="rounded-2xl w-11/12 text-lg font-semibold -translate-y-8 bg-gray-900 text-white p-6 z-20">
                      {item[0]}
                    </p>
                  </div>
                ))}
              </div>
              <div className="text-white flex gap-4">
                <button
                  className={`${page === 1 ? "hidden" : ""}`}
                  onClick={() => setPage((prevPage) => Math.max(prevPage - 1, 1))}
                >
                  Previous
                </button>
                <button 
                  className={`${page === 42 ? "hidden" : ""}`}
                  onClick={() => setPage((prevPage) => prevPage + 1)}
                >
                  Next
                </button>
              </div>
            </>
          )}
        </>
      )}
    </main>
  );
};

export default HomePage;
