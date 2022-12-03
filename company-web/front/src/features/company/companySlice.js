import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const apiUrl = "http://3.21.35.240:1337/";

export const fetchAsynCampanyList_Get = createAsyncThunk("company_list/get", async () => {
    const res = await axios.get(`${apiUrl}api/company/`, {
      headers: { 
      },
    });
    return res.data;
});

export const fetchAsynCampany_Get = createAsyncThunk("company_info/get", async (id) => {
    const res = await axios.get(`${apiUrl}api/company/${id}`, {
      headers: { 
      },
    });
    return res.data;
});

const companySlice = createSlice({
    name: 'company',
    initialState: {
        company_list: [{id: '', name: '', category: '', keywords: {}, news: {}, recruit: {}}, ],
        company_info: {id: '', name: '', category: '', keywords: {}, news: {}, recruit: {}},
    },
    reducers: {
    
    },
    extraReducers: (builder) => {
        builder.addCase(fetchAsynCampanyList_Get.fulfilled, (state, action) => {
            state.company_list = action.payload;
        })
        builder.addCase(fetchAsynCampany_Get.fulfilled, (state, action) => {
            state.company_info = action.payload;
        })
    }
})

export const { } = companySlice.actions;
export const selectCompany_list = (state) => state.company.company_list;
export const selectCompany_info = (state) => state.company.company_info;

export default companySlice.reducer;

