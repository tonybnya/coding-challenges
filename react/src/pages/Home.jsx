import ModalChallenge from "../components/ModalChallenge";
import challenges from "../challenges.js";

const Home = () => {
  return (
    <div className="bg-[#030713] text-white min-h-screen px-4 sm:px-6 lg:px-20 mt-10">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2 p-2 place-items-center bg-[#1C202A] rounded-md">
        {challenges.map((challenge, index) => (
          <ModalChallenge key={index} challenge={challenge} />
        ))}
      </div>
    </div>
  );
};

export default Home;
