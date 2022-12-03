import React, { createContext, useState, useEffect, memo } from "react";
import { withCookies } from "react-cookie";
import axios from "axios";
export const ApiContext = createContext();

const ApiContextProvider = (props) => {
    const token = props.cookies.get('current-token');
    const [memos, setMemos] = useState([])
    const [editedMemo, setEditedMemo] = useState({id: '', title: '', memo: ''})
    const [cover, setCover] = useState([])
    const [modalIsOpen, setModalIsOpen] = useState(false);
    const [selectedMemo, setSelectedMemo] = useState([])


    useEffect(() => {
        const getMemoList = async () => {
            try {
                const res = await axios.get(
                    'http://127.0.0.1:8000/blog/',
                    {
                        headers: {
                            Authorization: `Token ${token}`,
                        },
                    }
                );
                setMemos(res.data);
            } catch {
                console.log('error')
            }
        };
        getMemoList();
    }, [token, selectedMemo.id])

    const deleteMemo = async () => {
        try{
            await axios.delete(
                `http://127.0.0.1:8000/blog/${selectedMemo.id}/`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Token ${token}`,
                    }
                }
            );
            setEditedMemo([])
            setCover([])
            setMemos(memos.filter((dev)=>dev.id !== selectedMemo.id))
            setSelectedMemo([])
        } catch {
            console.log('error')
        }
    }

    const createMemo = async () => {
        const createData = new FormData();
        createData.append('title', editedMemo.title)
        createData.append('memo', editedMemo.memo)
        createData.append('img', cover)
        try {
            const res = await axios.post(
                'http://127.0.0.1:8000/blog/create',
                createData,
                {
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Token ${token}`,
                    },
                }
            );
            setMemos([...memos, res.data])
            setEditedMemo([])
            setCover([])
            setModalIsOpen(false)
        } catch {
            console.log('error')
        }
    }

    const editMemo = async () => {
        const editData = new FormData();
        editData.append('title', editedMemo.title)
        editData.append('memo', editedMemo.memo)
        editData.append('img', cover)
        try {
            const res = await axios.put(
                `http://127.0.0.1:8000/blog/${selectedMemo.id}/`,
                editData,
                {
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: `Token ${token}`,
                    }
                }
            )
            setSelectedMemo(res.data)
            setEditedMemo([])
            setCover([])
            setModalIsOpen(false)

        } catch {
            console.log('error')
        }
    }

return (
    <ApiContext.Provider
      value={{
        memos,
        createMemo,
        editedMemo,
        setEditedMemo,
        cover, 
        setCover,
        modalIsOpen, 
        setModalIsOpen,
        setSelectedMemo,
        selectedMemo,
        deleteMemo,
        editMemo
      }}
    >
      {props.children}
    </ApiContext.Provider>
  );
};


export default withCookies(ApiContextProvider);