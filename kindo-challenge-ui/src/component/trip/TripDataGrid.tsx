import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button } from '@mui/material';
import {useEffect, useState} from "react";
import TripDetailService from "../services/TripDetailService";
import {TripDetail} from "../types";


export default function
    TripDataGrid({handleRegister}:any) {

    const [rows, setRows] = useState<TripDetail[]>([]);
    useEffect(() => {
        TripDetailService.getAllTripDetails().then((response) => {
            if (response) {
                if(response.length>0){
                    setRows(response)
                }
            } else {
                console.log("No rows found in getAllTripDetails!")
            }
        }).catch((ex) => {
            console.log("Error in getAllTripDetails")
            console.log(ex)
        });
    },[]);


    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell>Trip Name</TableCell>
                        <TableCell align="center">Trip Location</TableCell>
                        <TableCell align="center">School Name</TableCell>
                        <TableCell align="center">Grade</TableCell>
                        <TableCell align="center">Date</TableCell>
                        <TableCell align="center">Cost (NZD)</TableCell>
                        <TableCell align="center">Action</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.length>0 && rows.map((row) => (
                        <TableRow
                            key={row.trip_name}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {row.trip_name}
                            </TableCell>
                            <TableCell align="center">{row.trip_location}</TableCell>
                            <TableCell align="center">{row.school? row.school.school_name : ''}</TableCell>
                            <TableCell align="center">{row.grade}</TableCell>
                            <TableCell align="center">{row.date}</TableCell>
                            <TableCell align="center">${row.cost.toFixed(2)}</TableCell>
                            <TableCell align="center">
                                <Button
                                    variant="contained"
                                    color="primary"
                                    onClick={() => handleRegister(row)}
                                >
                                    Register
                                </Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}