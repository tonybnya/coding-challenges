import { CheckCircle, Github } from "lucide-react";
import { Button } from "@/components/ui/button";

const CardChallenge = ({
  id,
  icon,
  title,
  description,
  src,
  live,
  tags = [],
}) => {
  return (
    <div className="max-w-sm p-4 bg-[#030710] rounded-md">
      <div className="flex items-center justify-between pb-4">
        <img
          src={icon}
          alt={`Icon for ${title}`}
          className="h-8 w-8 object-contain"
        />
        <div className="flex gap-2">
          {live ? (
            <a
              target="_blank"
              href={live}
              className="hover:scale-105 transition-transform duration-200"
            >
              <CheckCircle className="w-4 h-4 text-red-500 animate-pulse" />
            </a>
          ) : (
            <CheckCircle className="w-4 h-4 text-gray-500 opacity-50" />
          )}
          {src && (
            <a
              target="_blank"
              href={src}
              className="hover:scale-105 transition-transform duration-200"
            >
              <Github className="w-4 h-4 text-gray-200" />
            </a>
          )}
        </div>
      </div>
      <div>
        <h5 className="mb-2 text-2xl font-semibold tracking-tight text-gray-300">
          {title}
        </h5>
      </div>
      <p className="mb-3 font-normal text-gray-500">{description}</p>
      <div className="flex flex-wrap gap-2">
        {tags?.map((tag, i) => (
          <Button className="font-base" key={i}>
            {tag}
          </Button>
        ))}
      </div>
    </div>
  );
};

export default CardChallenge;
