import { useState, useEffect } from "react";
import ModalChallenge from "../components/ModalChallenge";

const API_URL = "http://localhost:8000/api";

const Home = () => {
  const [challenges, setChallenges] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchChallenges = async () => {
      setIsLoading(true);
      setError("");

      try {
        const response = await fetch(`${API_URL}/challenges/`);
        const data = await response.json();

        if (!data || data.length === 0) {
          throw new Error("No challenges found");
        }

        setChallenges(data);
      } catch (error) {
        console.error("Error:", error);
        setError("Failed to fetch challenges. Please try again later.");
        setChallenges([]);
      } finally {
        setIsLoading(false);
      }
    };

    fetchChallenges();
  }, []);

  if (isLoading) return <div className="text-center mt-10">Loading...</div>;
  if (error)
    return <div className="text-center text-red-500 mt-10">{error}</div>;

  return (
    <div className="bg-[#030713] text-white min-h-screen px-4 sm:px-6 lg:px-20 mt-10">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2 p-2 place-items-center bg-[#1C202A] rounded-md">
        {challenges.map((challenge) => (
          <ModalChallenge key={challenge.id} challenge={challenge} />
        ))}
      </div>
    </div>
  );
};

export default Home;
