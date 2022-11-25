import React from 'react';

const RecommendationList = React.lazy(() => import('../pages/Recommendation'));
const ChatUI = React.lazy(() => import('../pages/Landing'));

export interface RoutesProps {
    path: any;
    component?: any;
}

// root routes
const rootRoute: RoutesProps = {
    path: '/',
    component: ChatUI,
};

const recommendationRoute: RoutesProps = {
    path: '/recommendation',
    component: RecommendationList,
};

export { rootRoute, recommendationRoute };