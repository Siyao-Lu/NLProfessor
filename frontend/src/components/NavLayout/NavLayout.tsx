import Container from "react-bootstrap/Container";
import { Outlet, Link } from "react-router-dom";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

const NavLayout = () => {
  return (
    <>
      <Navbar bg="light" variant="light">
        <Container className="nav-bar">
          <Navbar.Brand>NLProfessor</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">
              Home
            </Nav.Link>
            <Nav.Link as={Link} to="/chat">
              Chat
            </Nav.Link>
            <Nav.Link as={Link} to="/recommendations">
              Recommendations
            </Nav.Link>
          </Nav>
          <Nav>
            <Nav.Link href="https://github.com/SonyaInSiberia/NLProfessor">
              <i className="bi bi-box-arrow-up-right"></i> GitHub
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <Outlet />
    </>
  );
};

export default NavLayout;
