import React from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';

interface userInput {
    user_input: string;
}

export default function UserInputBar() {
    const { register, handleSubmit } = useForm<userInput>();
    const onSubmit: SubmitHandler<userInput> = data => {
        console.log(data);
        // send to backend 
    };

    return (
        <div className="userInputBar">
            <form onSubmit={handleSubmit(onSubmit)}>
                <label>user input</label>
                <input {...register("user_input")}
                    placeholder="type your concerns!" />
                <input type="submit" />
            </form>
            {/* <button type="button" onClick={handleSubmit(onSubmit)}>
                submit
            </button> */}
        </div>
    );

};