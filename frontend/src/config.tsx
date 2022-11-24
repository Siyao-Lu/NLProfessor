// Config starter code
import YearOptions from "./components/YearOptions/YearOptions";

const config = {
  botName: "LearningBot",
  initialMessages: [],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#376B7E",
    },
    chatButton: {
      backgroundColor: "#376B7E",
    },
  },
  widgets: [
    {
      widgetName: "learningOptions",
      widgetFunc: (props: any) => <YearOptions {...props} />,
    },
  ],
};

export default config;
