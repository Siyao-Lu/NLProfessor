import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { rootRoute, recommendationRoute } from './index';

const Routing = () => {
    return (
        <Routes>
            <Route path={String(rootRoute['path'])} element={rootRoute['component']}>
                <Route index element={rootRoute['component']} />
                <Route
                    path={String(recommendationRoute['path'])}
                    element={recommendationRoute['component']}
                />
            </Route>
        </Routes>
    );
};

export default Routing;
